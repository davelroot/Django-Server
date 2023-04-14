from unicodedata import category
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, reverse
from .models import Briefingapplication, Briefinglojavirtual, Briefingwebsites, Logotiposglass
from django.contrib import messages
from .forms import Briefing_lojavirtualFrom, Briefing_frontendFrom, Briefing_mobileFrom

# Create your views here.

class MmainHomeView(TemplateView):
    template_name = 'seo_agency/index.html'

def error_403(request, exception):
	data = {}
	return render(request, 'errous/403.html', data)


def error_404(request, exception):
	data = {}
	return render(request, 'errous/404.html', data)


def error_500(request, exception=None):
	data = {}
	return render(request, 'errous/500.html', data)




def Developerback(request):

    logotipos = Logotiposglass.objects.all()
    form = Briefing_lojavirtualFrom()
    if request.method == "POST":
        form = Briefing_lojavirtualFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainHome:developerback')				
	#messages.success(request, "Formulario Aceite, Verifique o seu Email")
    return render(request,'seo_agency/desenvolvimentos/developerback.html',{'form':form})



def Developerfront(request):

    logotipos = Logotiposglass.objects.all()
    form = Briefing_frontendFrom()
    if request.method == "POST":
        form = Briefing_frontendFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainHome:developerback')				
	#messages.success(request, "Formulario Aceite, Verifique o seu Email")
    return render(request,'seo_agency/desenvolvimentos/developerfront.html',{'form':form})


def Developermobile(request):
    
    form = Briefing_mobileFrom()
    if request.method == "POST":
        form = Briefing_mobileFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainHome:developermobile')				
	#messages.success(request, "Formulario Aceite, Verifique o seu Email")
    return render(request,'seo_agency/desenvolvimentos/developerMobile.html',{'form':form})



def NetFlix(request):
    logotipos = Logotiposglass.objects.all()
    return render(request,'seo_agency/netFlix.html')


def HospedagemAll(request):
    logotipos = Logotiposglass.objects.all()
    return render(request,'seo_agency/hospedagemrevenda/hospedagemAll.html')


def AssistAcessorios(request):
    logotipos = Logotiposglass.object.all()
    return render(request,"seo_agency/acessorios/AssistAcessorios.html", logotipos=logotipos)


def DesigerGrafico(request):
    logotipos = Logotiposglass.objects.all()
    return render(request, 'seo_agency/designer/desigerGrafico.html')


def SocialMedia(request):
    model = Logotiposglass
    logotipos = Logotiposglass.objects.all()
    return render(request, 'seo_agency/marketing/socialMedia.html')


def AssistenciaTecnica(request):
    logotipos = Logotiposglass.objects.all()
    
    return render(request, 'seo_agency/assistencia/AssistenciaTecnica.html')


def EventosAll(request):
    logotipos = Logotiposglass.objects.all()
    return render(request, 'seo_agency/eventos/eventosAll.html')


def Softgestao(request):
    logotipos = Logotiposglass.objects.all()
    return render(request, 'seo_agency/somafix/softgestao.html')


def Jogosfull(request):
    logotipos = Logotiposglass.objects.all()
    return render(request, 'seo_agency/games/jogosfull.html')


def Servicosnstalacaomanutecao(request):
    logotipos = Logotiposglass.objects.all()
    return render(request, 'seo_agency/manutecoes/servicosnstalacaomanutecao.html')

def About(request):
    logotipos = Logotiposglass.objects.all()
    return render(request,'seo_agency/about.html')


def Contact(request):
    logotipos = Logotiposglass.objects.all()
    return render(request,'seo_agency/contacts.html')


#@login_required
#def home(request):
#    posts = Post.objects.all()
#    return render(request,"home.html", user=current_user, posts=posts)


#@login_required
#def create_post(request):
#    if request.method == "POST":
#        text = request.form.get('text')

#        if not text:
#            flash('Post cannot be empty', category='error')
#        else:
#            post = Post(text=text, author=current_user.id)
#            db.session.add(post)
#            db.session.commit()
#            flash('Post created!', category='success')
#            return redirect(url_for('views.home'))

#    return render(request,'create_post.html', user=current_user)



#@login_required
#def delete_post(request, id):
#    post = Post.objects.filter_by(id=id).first()

#    if not post:
#        flash("Post does not exist.", category='error')
#    elif current_user.id != post.id:
#        flash('You do not have permission to delete this post.', category='error')
#    else:
#        db.session.delete(post)
#        db.session.commit()
#        flash('Post deleted.', category='success')

#    return redirect(url_for('views.home'))



#@login_required
#def posts(request, username):
#    user = User.objects.filter_by(username=username).first()

#    if not user:
#        flash('No user with that username exists.', category='error')
#        return redirect(url_for('views.home'))
#
#    posts = user.posts
#    return render(request,"posts.html", user=current_user, posts=posts, username=username)


#@main.route("/create-comment/<post_id>", methods=['POST'])
#@login_required
#def create_comment(post_id):
#    text = request.form.get('text')
#
#    if not text:
#        flash('Comment cannot be empty.', category='error')
#    else:
#        post = Post.objects.filter_by(id=post_id)
#        if post:
#            comment = Comment(
#                text=text, author=current_user.id, post_id=post_id)
#            db.session.add(comment)
#            db.session.commit()
 #       else:
#            flash('Post does not exist.', category='error')

#    return redirect(url_for('views.home'))


#@main.route("/delete-comment/<comment_id>")

#def delete_comment(comment_id):
#    comment = Comment.objects.filter_by(id=comment_id).first()
#
#    if not comment:
#        flash('Comment does not exist.', category='error')
#    elif current_user.id != comment.author and current_user.id != comment.post.author:
#        flash('You do not have permission to delete this comment.', category='error')
#    else:
#        db.session.delete(comment)
#        db.session.commit()
#
#    return redirect(url_for('views.home'))


#@main.route("/like-post/<post_id>", methods=['POST'])

#def like(post_id):
#    post = Post.objects.filter_by(id=post_id).first()
#    like = Like.objects.filter_by(
#        author=current_user.id, post_id=post_id).first()
#
#    if not post:
#        return jsonify({'error': 'Post does not exist.'}, 400)
#    elif like:
#        db.session.delete(like)
 #       db.session.commit()
 #   else:
 #       like = Like(author=current_user.id, post_id=post_id)
 #       db.session.add(like)
#db.session.commit()
#
#    return jsonify({"likes": len(post.likes), "liked": current_user.id in map(lambda x: x.author, post.likes)})
#