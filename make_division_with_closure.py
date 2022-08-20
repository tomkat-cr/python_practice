# make_division_with_closure.py
# 2022-07-02 | CR

def make_division_by(n):
  """This closure returns a function the returs the division
     of an x number by n
  """
  # you have to code here
  def perform_division(x):
    return x/n
  return perform_division

division_by_3 = make_division_by(3)
print(division_by_3(18)) # the expected output is 6

division_by_5 = make_division_by(5)
print(division_by_5(100)) # the expected output is 20

division_by_18 = make_division_by(18)
print(division_by_18(54)) # the expected output is 3
