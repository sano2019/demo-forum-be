class Merger:
    @classmethod
    def merge(cls, fields, source, target, target_prepender):
        updated_fields = []
        for field in fields:
            target_field_name = '{}_{}'.format(target_prepender, field)
            setattr(target, target_field_name, getattr(source, field))
            updated_fields.append(target_field_name)
        return updated_fields
