from flask import Blueprint

ArticleModule=Blueprint("Article_BP",__name__,static_folder="static",template_folder="templates")

from .views import edit_article



