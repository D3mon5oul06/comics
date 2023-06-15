import graphene
from graphene_django import DjangoObjectType
from myapp.models import DataEntry

class DataEntryType(DjangoObjectType):
    class Meta:
        model = DataEntry

class Query(graphene.ObjectType):
    all_data_entries = graphene.List(DataEntryType)
    data_entries_by_user = graphene.List(DataEntryType, user=graphene.String(required=True))
    data_entries_by_model = graphene.List(DataEntryType, model=graphene.String(required=True))

    def resolve_all_data_entries(self, info):
        return DataEntry.objects.all()
    
    def resolve_data_entries_by_user(self, info, user):
        return DataEntry.objects.filter(user=user)
    
    def resolve_data_entries_by_model(self, info, model):
        return DataEntry.objects.filter(model=model)
    

class CreateDataEntry(graphene.Mutation):
    id = graphene.Int()
    user = graphene.String()
    model = graphene.String()
    prompt = graphene.String()
    result = graphene.String()

    class Arguments:
        user = graphene.String()
        model = graphene.String()
        prompt = graphene.String()
        result = graphene.String()

    def mutate(self, info, user, model, prompt, result):
        data_entry = DataEntry(user=user, model=model, prompt=prompt, result=result)
        data_entry.save()

        return CreateDataEntry(
            id=data_entry.id,
            user=data_entry.user,
            model=data_entry.model,
            prompt=data_entry.prompt,
            result=data_entry.result,
        )
    
class Mutation(graphene.ObjectType):
    create_data_entry = CreateDataEntry.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)