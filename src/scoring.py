# src/scoring.py


def calculate_labor_market_score(unemployment_rate):
    """
    Lower unemployment generally means
    a stronger labor market.

    Returns:
        score from 0-100
    """

    if unemployment_rate <= 3.5:
        return 100

    elif unemployment_rate <= 4:
        return 90

    elif unemployment_rate <= 5:
        return 75

    elif unemployment_rate <= 6:
        return 55

    elif unemployment_rate <= 7:
        return 35

    else:
        return 15


def calculate_inflation_score(inflation_rate):
    """
    Moderate inflation is healthiest.

    Returns:
        score from 0-100
    """

    if 1.5 <= inflation_rate <= 2.5:
        return 100

    elif 2.5 < inflation_rate <= 3:
        return 85

    elif 1 <= inflation_rate < 1.5:
        return 75

    elif 3 < inflation_rate <= 4:
        return 60

    elif 4 < inflation_rate <= 6:
        return 35

    else:
        return 15


def calculate_interest_rate_score(fed_funds_rate):
    """
    Moderate rates are generally healthiest.

    Returns:
        score from 0-100
    """

    if 2 <= fed_funds_rate <= 5:
        return 100

    elif 0 <= fed_funds_rate < 2:
        return 75

    elif 5 < fed_funds_rate <= 6:
        return 65

    elif 6 < fed_funds_rate <= 8:
        return 40

    else:
        return 20


def calculate_macropulse_score(
    unemployment_rate,
    inflation_rate,
    fed_funds_rate
):
    """
    Main MacroPulse composite score.

    Final score ranges from 0-100.
    """

    labor_score = calculate_labor_market_score(
        unemployment_rate
    )

    inflation_score = calculate_inflation_score(
        inflation_rate
    )

    rate_score = calculate_interest_rate_score(
        fed_funds_rate
    )

    # Weighting system
    # Labor market: 40%
    # Inflation:   35%
    # Rates:       25%

    macropulse_score = (
        labor_score * 0.40 +
        inflation_score * 0.35 +
        rate_score * 0.25
    )

    results = {
        "labor_market_score": round(labor_score, 1),
        "inflation_score": round(inflation_score, 1),
        "interest_rate_score": round(rate_score, 1),
        "macropulse_score": round(macropulse_score, 1)
    }

    return results


def classify_macropulse_environment(score):
    """
    Convert MacroPulse score into label.
    """
    if score >= 85:
        return "Strong Expansion"

    elif score >= 70:
        return "Stable Expansion"

    elif score >= 55:
        return "Slowing Growth"

    elif score >= 40:
        return "Economic Weakness"

    else:
        return "High Recession Risk"
    
def get_letter_grade(score):
    """
    Convert MacroPulse score into a letter grade.
    """
    if score >= 97:
        return "A+"

    elif score >= 93:
        return "A"

    elif score >= 90:
        return "A-"

    elif score >= 87:
        return "B+"

    elif score >= 83:
        return "B"

    elif score >= 80:
        return "B-"

    elif score >= 77:
        return "C+"

    elif score >= 73:
        return "C"

    elif score >= 70:
        return "C-"

    elif score >= 67:
        return "D+"

    elif score >= 63:
        return "D"

    elif score >= 60:
        return "D-"

    else:
        return "F"