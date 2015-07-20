"Assorted class utilities and tools"

class AttrDisplay:
	"""
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """
    def gatherAttrs(self):
    	attrs = []
    	for key in sorted(self.__dict__):
    		attrs.append('%s=%s' % (key, getattr(self, key)))