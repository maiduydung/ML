import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor

# forward method for variable selection based on AIC.
# Stepwise feature selection method (forward); 変数増加法による変数選択
def step_aic_forward(model, exog, endog, **kwargs):
    '''
    This function calculates the best subset of explanatory (exogenous) variables based on AIC.
    Both exog and endog can be either str or list.

    Arguments:
        model: model from statsmodels.formula.api
        exog (str or list): explanatory (exogenous) variables
        endog (str or list): objective (endogenous) variables
        kwargs: additional keyword argments for model (data, family, ...)

    Return values:
        model: a model with the smallest AIC
    '''

    # Convert exog, endog into 1-d list
    exog = np.r_[[exog]].flatten()
    endog = np.r_[[endog]].flatten()
    remaining = set(exog)
    selected = []  # Selected exogenous variables

    # First, calculate AIC with a constant (no exogs)
    formula_head = ' + '.join(endog) + ' ~ '
    formula = formula_head + '1'
    aic = model(formula=formula, **kwargs).fit().aic
    print('AIC: {:.3f}, formula: {}'.format(aic, formula))

    current_score, best_new_score = aic, aic

    # Break loop if all exogs are selected or no remaining exogs can improve AIC
    while True:
        score_with_candidates = []
        for candidate in remaining:
            # Calculate AIC for adding an exog one by one
            formula_tail = ' + '.join(selected + [candidate])
            formula = formula_head + formula_tail
            aic = model(formula=formula, **kwargs).fit().aic
            print('AIC: {:.3f}, formula: {}'.format(aic, formula))

            score_with_candidates.append((aic, candidate))

        # Select best_candidate with minimum AIC
        score_with_candidates.sort()
        best_score, best_candidate = score_with_candidates[0]

        # select best_candidate if AIC is improved
        improved = False
        if best_score < current_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_score
            improved = True
            
        if not remaining or not improved: break

    formula = formula_head + ' + '.join(selected)
    print('The best formula: {}'.format(formula))
    aic = model(formula=formula, **kwargs).fit().aic
    print('Minimum AIC: {:.3f}'.format(aic))
    return model(formula, **kwargs).fit()


def calc_vifs(X, y):
    model = sm.OLS(y, sm.add_constant(X))
    results = model.fit()
    n_cols = model.exog.shape[1]
    vifs_list = [variance_inflation_factor(model.exog,i) for i in range(n_cols)]
    vifs = pd.DataFrame(vifs_list, index=model.exog_names, columns=['VIF'])
    return vifs
