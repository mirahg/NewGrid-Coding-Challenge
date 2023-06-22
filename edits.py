# Mirah Gordon
# Coding Challenge Submission

# there are 5 edit classes defined
# BranchClosedStatusEdit, BranchMonitoredInputEdit, BranchLimitEdit, UserDefinedConstraintMonitoredInputEdit, UserDefinedConstraintLimitEdit
# refactor this code with the objective of making it more pythonic and easier to understand
# making the code more performant is not the main objective
class OrigBranchClosedStatusEdit:

    entity_name: str = 'branch'
    type = bool

    def __init__(self, affected_object, value: bool) -> None:

        self._affected_object = affected_object
        self._value = value


    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and self._affected_object == other.affected_object


    @property
    def affected_object(self):
        return self._affected_object


class OrigBranchMonitoredInputEdit:

    entity_name: str = 'branch'
    type = bool

    def __init__(self, affected_object, value: bool) -> None:

        self._affected_object = affected_object
        self._value = value


    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and self._affected_object == other.affected_object


    @property
    def affected_object(self):
        return self._affected_object


class OrigBranchLimitEdit:

    entity_name: str = 'branch'
    type = float

    def __init__(self, affected_object, value: bool) -> None:

        self._affected_object = affected_object
        self._value = value


    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and self._affected_object == other.affected_object


    @property
    def affected_object(self):
        return self._affected_object


class OrigUserDefinedConstraintMonitoredInputEdit:

    entity_name: str = 'user_defined_constraint'
    type = bool

    def __init__(self, affected_object, value: bool) -> None:

        self._affected_object = affected_object
        self._value = value


    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and self._affected_object == other.affected_object


    @property
    def affected_object(self):
        return self._affected_object


class OrigUserDefinedConstraintLimitEdit:

    entity_name: str = 'user_defined_constraint'
    type = float

    def __init__(self, affected_object, value: bool) -> None:

        self._affected_object = affected_object
        self._value = value


    def __eq__(self, other) -> bool:
        return isinstance(other, self.__class__) and self._affected_object == other.affected_object


    @property
    def affected_object(self):
        return self._affected_object

# my refactoring
# in the original code for the 5 classes, there is a lot of unnecessary repition 
# e.g. the init, eq, and affected_object methods all being the same
# this is the perfect place to employ object-oriented principles: namely inheritance 
# to do this, let's create a base class and have each individual class inherit from it
class BaseEdit:

    def __init__(self, affected_object, value) -> None:

        self._affected_object = affected_object
        self._value = value
    
    # we can simplify the eq method by comparing other to type(self) instead of self.__class__
    def __eq__(self, other) -> bool:
        return isinstance(other, type(self)) and self._affected_object == other.affected_object

    @property
    def affected_object(self):
        return self._affected_object

# now that we have a base class with those methods defined, we can define the 5 edit classes
# this is where we can specify the entity_name and type 

# as a note, I've renamed all of the classes to denote the original and refactored class as different for testing purposes 
# in industry, this would be tracked through version control and wouldn't be necessary 
class RefactoredBranchClosedStatusEdit(BaseEdit):

    entity_name: str = 'branch'
    type = bool

class RefactoredBranchMonitoredInputEdit(BaseEdit):

    entity_name: str = 'branch'
    type = bool

class RefactoredBranchLimitEdit(BaseEdit):

    entity_name: str = 'branch'
    type = float

class RefactoredUserDefinedConstraintMonitoredInputEdit(BaseEdit):

    entity_name: str = 'user_defined_constraint'
    type = bool

class RefactoredUserDefinedConstraintLimitEdit(BaseEdit):

    entity_name: str = 'user_defined_constraint'
    type = float 

# as we can see, the code is significantly easier to understand and takes advantage of python being an object oriented program 
# we were able to reduce code duplication and improve readability

# now let's create some unit tests to ensure that fucntionality has been preserved
import unittest

# create a class to store all the methods for testing 
class TestEditClasses(unittest.TestCase):
    def test_branch_closed_status_edit(self):
        obj1, obj2 = object(), object()

        # original code
        orig_edit1 = OrigBranchClosedStatusEdit(obj1, True)
        orig_edit2 = OrigBranchClosedStatusEdit(obj1, False)
        orig_edit3 = OrigBranchClosedStatusEdit(obj2, True)

        # refactored code
        refactored_edit1 = RefactoredBranchClosedStatusEdit(obj1, True)
        refactored_edit2 = RefactoredBranchClosedStatusEdit(obj1, False)
        refactored_edit3 = RefactoredBranchClosedStatusEdit(obj2, True)

        self.assertEqual(orig_edit1.affected_object, 
                         refactored_edit1.affected_object)
        self.assertEqual(orig_edit2.affected_object,
                         refactored_edit2.affected_object)
        self.assertEqual(orig_edit3.affected_object,
                         refactored_edit3.affected_object)

        self.assertEqual(orig_edit1 == orig_edit2,
                         refactored_edit1 == refactored_edit2)
        self.assertEqual(orig_edit1 == orig_edit3,
                         refactored_edit1 == refactored_edit3)

    def test_branch_monitored_input_edit(self):
        obj1, obj2 = object(), object()

        # original code
        orig_edit1 = OrigBranchMonitoredInputEdit(obj1, True)
        orig_edit2 = OrigBranchMonitoredInputEdit(obj1, False)
        orig_edit3 = OrigBranchMonitoredInputEdit(obj2, True)

        # refactored code
        refactored_edit1 = RefactoredBranchMonitoredInputEdit(obj1, True)
        refactored_edit2 = RefactoredBranchMonitoredInputEdit(obj1, False)
        refactored_edit3 = RefactoredBranchMonitoredInputEdit(obj2, True)

        self.assertEqual(orig_edit1.affected_object, 
                         refactored_edit1.affected_object)
        self.assertEqual(orig_edit2.affected_object,
                         refactored_edit2.affected_object)
        self.assertEqual(orig_edit3.affected_object,
                         refactored_edit3.affected_object)

        self.assertEqual(orig_edit1 == orig_edit2,
                         refactored_edit1 == refactored_edit2)
        self.assertEqual(orig_edit1 == orig_edit3,
                         refactored_edit1 == refactored_edit3)

    def test_branch_limit_edit(self):
        obj1, obj2 = object(), object()

        # original code
        orig_edit1 = OrigBranchLimitEdit(obj1, 10.0)
        orig_edit2 = OrigBranchLimitEdit(obj1, 30.0)
        orig_edit3 = OrigBranchLimitEdit(obj2, 10.0)

        # refactored code
        refactored_edit1 = RefactoredBranchLimitEdit(obj1, 10.0)
        refactored_edit2 = RefactoredBranchLimitEdit(obj1, 30.0)
        refactored_edit3 = RefactoredBranchLimitEdit(obj2, 10.0)

        self.assertEqual(orig_edit1.affected_object,
                         refactored_edit1.affected_object)
        self.assertEqual(orig_edit2.affected_object,
                         refactored_edit2.affected_object)
        self.assertEqual(orig_edit3.affected_object,
                         refactored_edit3.affected_object)

        self.assertEqual(orig_edit1 == orig_edit2,
                         refactored_edit1 == refactored_edit2)
        self.assertEqual(orig_edit1 == orig_edit3,
                         refactored_edit1 == refactored_edit3)

    def test_user_defined_constraint_monitored_input_edit(self):
        obj1, obj2 = object(), object()

        # original code
        orig_edit1 = OrigUserDefinedConstraintMonitoredInputEdit(obj1, True)
        orig_edit2 = OrigUserDefinedConstraintMonitoredInputEdit(obj1, False)
        orig_edit3 = OrigUserDefinedConstraintMonitoredInputEdit(obj2, True)

        # refactored code
        refactored_edit1 = RefactoredUserDefinedConstraintMonitoredInputEdit(obj1, True)
        refactored_edit2 = RefactoredUserDefinedConstraintMonitoredInputEdit(obj1, False)
        refactored_edit3 = RefactoredUserDefinedConstraintMonitoredInputEdit(
            obj2, True)

        self.assertEqual(orig_edit1.affected_object,
                         refactored_edit1.affected_object)
        self.assertEqual(orig_edit2.affected_object,
                         refactored_edit2.affected_object)
        self.assertEqual(orig_edit3.affected_object,
                         refactored_edit3.affected_object)

        self.assertEqual(orig_edit1 == orig_edit2,
                         refactored_edit1 == refactored_edit2)
        self.assertEqual(orig_edit1 == orig_edit3,
                         refactored_edit1 == refactored_edit3)

    def test_user_defined_constraint_limit_edit(self):
        obj1, obj2 = object(), object()

        # original code
        orig_edit1 = OrigUserDefinedConstraintLimitEdit(obj1, 10.0)
        orig_edit2 = OrigUserDefinedConstraintLimitEdit(obj1, 30.0)
        orig_edit3 = OrigUserDefinedConstraintLimitEdit(obj2, 10.0)

        # refactored code
        refactored_edit1 = RefactoredUserDefinedConstraintLimitEdit(obj1, 10.0)
        refactored_edit2 = RefactoredUserDefinedConstraintLimitEdit(obj1, 30.0)
        refactored_edit3 = RefactoredUserDefinedConstraintLimitEdit(obj2, 10.0)

        self.assertEqual(orig_edit1.affected_object,
                         refactored_edit1.affected_object)
        self.assertEqual(orig_edit2.affected_object,
                         refactored_edit2.affected_object)
        self.assertEqual(orig_edit3.affected_object,
                         refactored_edit3.affected_object)

        self.assertEqual(orig_edit1 == orig_edit2,
                         refactored_edit1 == refactored_edit2)
        self.assertEqual(orig_edit1 == orig_edit3,
                         refactored_edit1 == refactored_edit3)


if __name__ == '__main__':
    unittest.main()


# a class `EditContainer` has been defined. its objective is to contain a number of edits of different types, defined
# above, and be able to quickly perform the operations defined by the publicly exposed API.
# for example, does it contain edits of a particular type (`has_edits_by_type`)?
# or does it contain this edit already (`has_edit`)?
# add code to this class with the objective of making it performant and easy to understand
class EditContainer:

    # define edits as a dictionary to hold the edit and its class 
    # key : edit class
    # value : list of edits
    def __init__(self) -> None:
        self._edits = {}


    # check if there are currently edits in the container
    def __bool__(self) -> bool:
        return bool(self._edits)


    @property
    def has_branch_closed_status_edits(self) -> bool:
        return RefactoredBranchClosedStatusEdit in self._edits


    # add a new edit class with edits
    def add(self, edit_class, edits) -> None:
        if edit_class not in self._edits:
            self._edits[edit_class] = []
        self._edits[edit_class].extend(edits)


    # remove all current edits in the container 
    def clear(self) -> None:
        self._edits.clear()


    # get all the edits of a specific edit class
    def get_edits_by_type(self, edit_class):
        return self._edits.get(edit_class, [])


    # check if a given edit is stored in the container
    def has_edit(self, edit) -> bool:
        for v in self._edits.values():
            if edit == v:
                return True
        return False


    # check if the container has edits of a specific edit class 
    def has_edits_by_type(self, edit_class) -> bool:
        return edit_class in self._edits
