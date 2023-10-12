from library import base
assert hasattr(base,'foo'),"your are fool"
class derived(base):
    def bar(self):
        return self.foo()
