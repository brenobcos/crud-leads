# Leads


***POST /leads***

Rota capaz de registrar um novo Lead no banco de dados.

Modelo de requisição:
```
{
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000"
}
```

Modelo de resposta:
```{
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000",
    "creation_date": "Fri, 10 Sep 2021 17:53:25 GMT",
    "last_visit": "Fri, 10 Sep 2021 17:53:25 GMT",
    "visits": 1
}
```
Os seguintes erros foram tratados:
E-mail e telefone único;
Telefone obrigatoriamente no formato (xx)xxxxx-xxxx.

Corpo da requisição obrigatoriamente apenas com name, email e phone, sendo todos os campos do tipo string.

***GET /leads***

Rota lista todos os LEADS por ordem de visitas, do maior para o menor.

Modelo de requisição:
```
GET - localhost:5000/leads
```
Os seguintes erros devem ser tratados:
Nenhum dado encontrado.

***PATCH /leads***

Sua rota deve atualizar apenas o valor de visits e last_visit em cada requisição. O email do Lead deve ser utilizado para encontrar o registro a ser atualizado.

A cada requisição o valor de visits é acrescentado em 1.
A cada requisição o valor de last_visit é atualizado para a data do request.
Modelo de requisição:
```
{
    "email": "john@email.com"
}
```

Os seguintes erros foram tratados:
Corpo da requisição obrigatoriamente apenas com email, deve ser uma string;
Nenhum dado encontrado.

**DELETE /leads**

Rota deleta um Lead específico. O email do Lead deve ser utilizado para encontrar o registro a ser deletado.

Modelo de requisição:
```
{
    "email": "john@email.com"
}
```
