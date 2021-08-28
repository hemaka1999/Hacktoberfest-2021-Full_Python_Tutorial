all([0]) # False
all([0,1]) # False
all([0, "", [1]]) # False
all([1, "a", [1]]) # True
any([0]) # False
any([0,1]) # True
any([0, "", [1]]) # True