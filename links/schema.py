import graphene
from graphene_django import DjangoObjectType
from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()
    #1
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    company = graphene.String()
    precio = graphene.String()
    country = graphene.String()
    calificacion = graphene.Int()
    dispositivo = graphene.String()
    dificultad = graphene.String()
    categoria = graphene.String()
    version = graphene.String()
    image = graphene.String()

    class Arguments:
        name = graphene.String()
        company = graphene.String()
        precio = graphene.String()
        country = graphene.String()
        calificacion = graphene.Int()
        dispositivo = graphene.String()
        dificultad = graphene.String()
        categoria = graphene.String()
        version = graphene.String()
        image = graphene.String()

    def mutate(self, info, name, company, precio, country, calificacion, dispositivo, dificultad, categoria, version, image):
        link = Link(name=name, company=company, precio=precio, country=country, calificacion=calificacion,
                    dispositivo=dispositivo, dificultad=dificultad, categoria=categoria, version=version, image=image)
        link.save()

        return CreateLink(
            id=link.id,
            name=link.name,
            company=link.company,
            precio=link.precio,
            country=link.country,
            calificacion=link.calificacion,
            dispositivo=link.dispositivo,
            dificultad=link.dificultad,
            categoria=link.categoria,
            version=link.version,
            image=link.image
        )
#4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()