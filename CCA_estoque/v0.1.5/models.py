from django.db import models
from django.contrib.auth.models import User

# *** TABELAS PARA PRODUTOS E SUAS DERIVAÇÕES *** #
class Marca(models.Model):
    descricao = models.TextField()
    ativo = models.BooleanField()

    def __str__(self):
        return self.descricao

class Grupo(models.Model):
    descricao = models.TextField()
    ativo = models.BooleanField()
    
    def __str__(self):
        return self.descricao

class Tipo_Produto(models.Model):
    descricao = models.TextField()
    ativo = models.BooleanField()

    def __str__(self):
        return self.descricao

class Medida(models.Model):
    descricao = models.TextField()
    ativo = models.BooleanField()

    def __str__(self):
        return self.descricao

class Core(models.Model):
    nome = models.TextField()
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    descricao = models.TextField()
    ativo = models.BooleanField()

    def __str__(self):
        return self.descricao

class Produto(model.Model):
    codigo_interno = models.CharField(max_lengh=20)
    descricao = models.TextField()
    unidade = models.CharField(max_lengh=20)
    codigo_debarras = models.PositiveIntegerField()
    id_marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    id_grupo = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING)
    embalagem = models.CharField(max_lengh=20)
    id_tipo_produto = models.ForeignKey(Tipo_Produto, on_delete=models.DO_NOTHING)
    estoque = models.models.PositiveIntegerField()
    estoque_minimo = models.PositiveIntegerField()
    local_estoque = models.CharField(max_lengh=20)
    estoque2 = models.models.PositiveIntegerField()
    local_estoque2 = models.CharField(max_lengh=20)
    defeito = models.models.PositiveIntegerField()
    local_defeito = models.CharField(max_lengh=20)
    custo = models.FloatField()
    margem = models.FloatField()
    preço = models.FloatField()
    suspende_compra = models.BooleanField()
    suspende_venda = models.BooleanField()
    id_usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING) #TODO: Verificar trocade User por Usuário
    id_operacao = models.ForeignKey(Kardex_Operacao, on_delete=models.DO_NOTHING)
    obs = models.TextField()
    data_cadastro = models.TextField()
    id_cor = models.ForeignKey(Core, on_delete=models.DO_NOTHING)
    id_medida = models.ForeignKey(Medida, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self

class Kardex(model.Model):
    data = models.DateTimeField()
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()
    unidade = models.PositiveIntegerField()
    id_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    id_operacao = models.ForeignKey(Kardex_Operacao, on_delete=models.DO_NOTHING)
    destinatario = models.CharField(max_lengh=20)
    id_usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING) #TODO: Verificar troca de User por Usuário
    id_empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self

class Kardex_Operacao(model.Model):
    descricao = models.TextField()
    ativo = models.BooleanField()
    entrada = models.DateTimeField()
    saida = models.DateTimeField()

    def __str__(self):
        return self

# *** TABELA PARA FORNECEDORES *** #
class Fornecedore(models.Model):
    razao_social = models.CharField(max_lengh=50)
    nome_fantasia = models.CharField(max_lengh=50)
    tipo = models.CharField(max_lengh=50)
    cnpj_cpf = models.CharField(max_lengh=20)
    ie_rg = models.CharField(max_lengh=20)
    endereco = models.CharField(max_lengh=100)
    numero = models.PositiveIntegerField()
    cep = models.CharField(max_lengh=10)
    bairro = models.CharField(max_lengh=50)
    cidade = models.CharField(max_lengh=50)
    estado = models.CharField(max_lengh=50)
    uf = models.CharField(max_lengh=5)
    contato = models.CharField(max_lengh=50)
    ddd = models.CharField(max_lengh=5)
    telefone = models.CharField(max_lengh=20)
    celular = models.CharField(max_lengh=20)
    email = models.EmailField(max_lengh=50)
    obs = models.TextField()
    ativo = models.BooleanField()

    def __str__(self):
        return self

# *** TABELA PARA CLIENTES *** #
class Cliente(models.Model):
    razao_social = models.CharField(max_lengh=20)
    nome_fantasia = models.CharField(max_lengh=20)
    tipo = models.CharField(max_lengh=50)
    cnpj_cpf = models.CharField(max_lengh=20)
    ie_rg = models.CharField(max_lengh=20)
    ra = models.CharField(max_lengh=20)
    endereco = models.CharField(max_lengh=100)
    numero = models.PositiveIntegerField()
    cep = models.CharField(max_lengh=10)
    bairro = models.CharField(max_lengh=50)
    cidade = models.CharField(max_lengh=50)
    estado = models.CharField(max_lengh=50)
    uf = models.CharField(max_lengh=2)
    contato = models.CharField(max_lengh=50)
    ddd = models.CharField(max_lengh=10)
    telefone = models.CharField(max_lengh=20)
    celular = models.CharField(max_lengh=20)
    email = models.EmailField(max_lengh=50)
    obs = models.TextField()
    ativo = models.BooleanField()

    def __str__(self):
        return self

# *** TABELAS PARA ACESSOS, USUARIOS E EMPRESAS *** #
class Acesso(models.Model):
    acesso = models.CharField(max_lengh=20)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    master = models.CharField(max_lengh=20)
    incluir = models.CharField(max_lengh=20)
    alterar = models.CharField(max_lengh=20)
    imprimir = models.CharField(max_lengh=20)
    imprimir = models.CharField(max_lengh=20)
    ativo = models.BooleanField()
    observacao = models.TextField()

    def __str__(self):
        return self

class Usuário(models.Model):
    nome = models.CharField(max_lengh=20)
    senha = models.CharField(max_lengh=20)
    id_departamento = models.CharField(max_lengh=20) # Não é chave estrangeira?
    id_empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    id_acesso = models.ForeignKey(Acesso, on_delete=models.DO_NOTHING)
    ativo = models.BooleanField()
    obs = models.TextField()

    def __str__(self):
        return self

class Empresa(models.Model):
    razao_social = models.CharField(max_lengh=50)
    nome_fantasia = models.CharField(max_lengh=50)
    cnpj = models.CharField(max_lengh=20)
    regime_tributario = models.CharField(max_lengh=20)
    endereco = models.CharField(max_lengh=100)
    numero = models.PositiveIntegerField()
    cep = models.CharField(max_lengh=10)
    bairro = models.CharField(max_lengh=50)
    cidade = models.CharField(max_lengh=50)
    estado = models.CharField(max_lengh=50)
    uf = models.CharField(max_lengh=5)
    pedido_venda = models.CharField(max_lengh=50)
    pedido_compra = models.CharField(max_lengh=50)
    padrão = models.CharField(max_lengh=50)
    ativo = models.BooleanField()
    contato = models.CharField(max_lengh=50)
    ddd = models.CharField(max_lengh=5)
    telefone = models.CharField(max_lengh=20)
    celular = models.CharField(max_lengh=20)
    email = models.CharField(max_lengh=50)
    versao = models.CharField(max_lengh=50)
    unidade = models.CharField(max_lengh=50)
    matriz_filial = models.CharField(max_lengh=50)

    def __str__(self):
        return sel
