def _41():
    class ToDicMixin:
        def to_dict(self):
            return self._traverse_dict(self.__dict__)

        def _traverse_dict(self, inst_dict):
            output = {}
            for k, v in inst_dict.items():
                output[k] = self._traverse(k, v)
            return output

        def _traverse(self, k, v):
            if isinstance(v, ToDicMixin):
                return v.to_dict()
            elif isinstance(v, dict):
                return self._traverse_dict(v)
            elif isinstance(v, list):
                return [self._traverse(k, i) for i in v]
            elif hasattr(v, '__dict__'):
                return self._traverse_dict(v.__dict__)
            else:
                return v

_41()
