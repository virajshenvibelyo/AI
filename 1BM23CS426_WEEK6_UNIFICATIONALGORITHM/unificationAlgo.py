def unify(x, y, subst=None):
    if subst is None:
        subst = {}

    print(f"Unifying {x} with {y}")
    
    # Step 1: If x or y is a variable or constant
    if is_variable(x):
        return unify_variable(x, y, subst)
    elif is_variable(y):
        return unify_variable(y, x, subst)
    elif isinstance(x, str) and isinstance(y, str):  # Both are constants
        if x == y:
            return subst  # Constants are equal
        else:
            print(f"Constant mismatch: {x} != {y}")
            return "FAILURE"  # Constants mismatch
    elif isinstance(x, list) and isinstance(y, list):  # Handle argument lists
        if len(x) != len(y):
            print(f"Length mismatch: {len(x)} != {len(y)}")
            return "FAILURE"
        else:
            for xi, yi in zip(x, y):
                subst = unify(xi, yi, subst)
                if subst == "FAILURE":
                    return "FAILURE"
            return subst
    else:
        print(f"Cannot unify {x} with {y}")
        return "FAILURE"

def unify_variable(var, x, subst):
    print(f"Unifying variable {var} with {x}")
    if var in subst:
        return unify(subst[var], x, subst)
    elif x in subst:
        return unify(var, subst[x], subst)
    elif occurs_check(var, x, subst):
        print(f"Occurs check failed: {var} in {x}")
        return "FAILURE"
    else:
        subst[var] = x
        return subst

def is_variable(x):
    # Define variables as single lowercase letters
    return isinstance(x, str) and len(x) == 1 and x.islower()
def occurs_check(var, x, subst):
    if var == x:
        return True
    elif isinstance(x, list):
        return any(occurs_check(var, xi, subst) for xi in x)
    elif x in subst:
        return occurs_check(var, subst[x], subst)
    else:
        return False

# Test Inputs
term1 = ['Eats', 'x', 'kjdsh', "kdfg"]
term2 = ['Eats', 'app', 'y', 'c']

result = unify(term1, term2)
print("Result:", result)
