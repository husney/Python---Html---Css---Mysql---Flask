from camelcase import CamelCase

c = CamelCase()
texto = "esta oración debe estar en CamelCase"

camelcase = c.hump(texto)
print(camelcase)
