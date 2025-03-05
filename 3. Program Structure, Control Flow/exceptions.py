# Exception categories
#   BaseException       
#
#       SystemExit              Raised on program exit e.g. sys.exit
#
#       KeyboardInterrupt       CTRL-C pressed
#
#       StopIteration           End of sequence iteration
#
#       Exception               Base class for all program-related errors.
#           ArithmeticError     Math-related errors
#           ImportError         Import-related errors
#           LookupError         Container lookup errors
#           OSError             System-related errors
#           ValueError          Value-related errors
#           UnicodeError        Unicode string encoding-related errors
#           AssertionError      Assertion failed
#           AttributeError      Obj doesn't have attribute
#           EOFError            End of file
#           MemoryError
#           NameError           Name not found in local/global namespace
#           NotImplementedError Unimplemented feature
#           RuntimeError        Generic "something bad happened"
#           TypeError           Operation applied to an object of the wrong type
#           UnboundLocalError   Usage of local var before assignment


# SystemExit is NOT a child of Exception, but of BaseException.
#   it's not caught via "except Exception"

# Handle multiple exceptions inside single handler
try:
    raise
except (ValueError, OSError) as e:
    pass # e is either ValueError or OSError
    # if type(e) is ValueError:
    #   ...

# Custom exceptions 
class MyException(Exception):
    def __init__(self, arg1, arg2):
        # Important to assign to "args"... (used in stacktrace printing)
        self.args = ( arg1, arg2 )

# Chained exception (Exception.__cause__)
def f():
    def spam():
        try:
            1 / 0
        except ArithmeticError as e:
            raise RuntimeError("Error") from e

    try:
        spam()
    except Exception as exc:
        pass
        # exc is the RuntimeError
        # exc.__cause__ holds the original ArithmeticError

# Unexpected exception (Exception.__context__)
def f():
    def spam():
        try:
            1 / 0
        except ArithmeticError as e:
            print(err) # raises NameError
    
    try:
        spam()
    except Exception as exc:
        pass
        # exc is the NameError
        # exc.__context__ holds the original ArithmeticError