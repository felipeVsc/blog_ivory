# Teste Técnico - Ivory

## Sistema de Blog

TODO:

[ ] Documentar requisitos
[ ] Construir diagrama ER
[ ] Back-end
[ ] Front-end

### Requisitos

* Blogs
    * O sistema terá mais de um blog
    * Para criar o seu blog, você precisará logar via Django Admin e criar o seu blog por lá

* Gestor do Blog
    * Login via Django Admin
    * Criar blog
    * Modificar as infos do blog
    * Postar no blog, podendo salvar como rascunho (criar action)
    * Editar postagem
    * Arquivar postagem (soft-delete)
    * Apagar postagem (hard-delete)

* Leitor 
    * Comentar em postagem
    * Curtir comentário


### Rotas

* Post
    * getAll
    * getSpecific
    * CRUD

* Replys
    * CR
    * getAll
    * getSpecific

* Blog
    * CRUD
    * get All
    