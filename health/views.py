from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import CommentForm, PostForm, EditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PostList(generic.ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('q') # category id / name
        categories = Category.objects.order_by("-name")
        if category is not None:
            if category.isnumeric():
                category = int(category)
                queryset = Post.objects.filter(status=1, category=category)
            else:
                queryset = Post.objects.filter(status=1, category__name=category)
        else:
            queryset = Post.objects.filter(status=1)
        
        # making the list of context to be used in the templates
        # context = {
        #     "posts":queryset
        #     "categories":categories
        # }
        context["posts"] = queryset
        context["categories"]=categories

        return context


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class CommentReply(View):

    def post(self, request, slug, slug1, *args, **kwargs):
        post = Post.objects.get(id=slug)
        parent_comment = Comment.objects.get(id=slug1)
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.parent = parent_comment
            comment.save()
        else:
            comment_form = CommentForm()

        return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostUpVote(LoginRequiredMixin, View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        is_downvote = False

        for vote in post.downvote.all():
            if vote == request.user:
                is_downvote = True
                break
        
        if is_downvote:
            post.downvote.remove(request.user)

        is_upvote = False

        for vote in post.upvote.all():
            if vote == request.user:
                is_upvote = True
                break
       
        if not is_upvote:
            post.upvote.add(request.user)
        else:
            post.upvote.remove(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostDownVote(LoginRequiredMixin, View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        is_upvote = False

        for vote in post.upvote.all():
            if vote == request.user:
                is_upvote = True
                break

        if is_upvote:
            post.upvote.remove(request.user)
       
        is_downvote = False

        for vote in post.downvote.all():
            if vote == request.user:
                is_downvote = True
                break  

        if not is_downvote:
            post.downvote.add(request.user)
        else:
            post.downvote.remove(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    # fields = '__all__'
    # summernote_fields = ('content',)

   
class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'slug', 'featured_image', 'excerpt', 'content']


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


