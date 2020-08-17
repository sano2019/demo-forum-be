from rest_framework.views import APIView
from rest_framework.response import Response


class EnumView(APIView):
    permission_classes = []
    fields = ('i18n',)
    excluded = []

    def get(self, *args, **kwargs):
        enums = self.enum_class.get_as_tuple_list()
        enums_sorted = sorted(enums, key=lambda enum: enum[1])
        context = []
        for enum in enums_sorted:
            _id = enum[1]
            if _id not in self.excluded:
                enum_context = {'id': _id}
                for field in self.fields:
                    enum_context[field] = getattr(self.enum_class, field)[_id]
                context.append(enum_context)
        return Response(context)


class ListToApiView(APIView):
    list_ = []

    def get(self, *args, **kwargs):
        new_list = []
        for item in self.list_:
            new_list.append({'code': str(item[0]), 'value': item[1]})
        return Response(new_list)
