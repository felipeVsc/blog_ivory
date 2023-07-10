# Teste Técnico - Ivory

## Sistema de Blog

Autor: Felipe Vasconcelos

Sistema de blog para o teste técnico da Ivory.

Foi desenvolvido uma API com Django REST framework, além de páginas HTML com Bootstrap e jQuery que realizam as requisições para a API, consumindo os endpoints.

Foi escolhida essa abordagem, em detrimento do uso dos Templates do Django, para um melhor desacoplamento entre back-end e front-end; além de uma melhor usabilidade do Django REST framework para a finalidade de uma API, de modo que a manutenção e adição de novas features, rotas, e páginas se tornasse mais fácil. 

Foi utilizado o Django Admin para o controle de certas ações.

### Vídeo de demonstração:

https://youtu.be/4nguA_sWzS8

### Tempo gasto

Em média, 15 horas divididas em Sábado, Domingo e Segunda.

## Observações:

Necessário ter instalado:
* django-cors-header
* djangorestframework
* django
* sqlite

Você pode utilizar o requirements.txt!

Os links do html estão estáticos para a porta 8000, padrão do Django, logo, são de uso obrigatório!

As atualizações não ocorrem em tempo real, sendo necessário dar um refresh na página.

Você pode clicar sempre em "Blogs" no navbar para ir para a página inicial, dado que o botão voltar do navegador pode não funcionar dada a forma "Single Page" que foi construído o front-end.

O arquivo "Modelagem ER.png" consta a modelagem utilizada no SQLITE.

### Requisitos

* Blogs
    * O sistema terá mais de um blog, porém um único blog por usuário
    * Qualquer pessoa pode criar o seu blog
    * Todos os blogs são públicos

* Gestor do Blog
    * Criar blog via interface e via Django Admin
    * Login via Django Admin
    * Modificar as informações do blog
    * Postar no blog, podendo salvar como rascunho (não publicado)
    * Actions do Django Admin para publicação
    * Editar postagem
    * Arquivar postagem (não publicado)
    
* Leitor 
    * Curtir uma postagem
    * Comentar em postagem
    * Curtir comentário

### Rotas

* Post
    * posts_get_all_from_blog_view
    * posts_find_by_id_view
    * posts_view
    * posts_like_view

* Replys
    * reply_view
    * reply_find_by_id_view
    * reply_get_all_view
    * reply_find_by_id_view
    * reply_get_likes_by_id_view
    * reply_likes_view

* Blog
    * blogs_view
    * blogs_find_by_id_view
    * author_view
    


