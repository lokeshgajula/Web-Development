from django.shortcuts import render
from django.conf import settings
from .models import Question
from .forms import QuestionForm
import wikipediaapi
# Create your views here.
def index(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			#try:
				question = form.cleaned_data['question']
				wiki_terms = form.cleaned_data['wiki_terms']

				wiki = wikipediaapi.Wikipedia('en')
				wiki_text = wiki.page(wiki_terms).summary

				result = settings.BERT_PIPELINE(question=question,context=wiki_text)
				answer = result['answer']
				prediction_score = result['score']

				q=Question()
				q.wiki_terms=wiki_terms
				q.wiki_text = wiki_text
				q.question = question
				q.answer = answer
				q.prediction_score = prediction_score
				q.save()
			#except:
			#	answer = 'There was an error!'
			#	prediction_score=0
		return render(request,'main/index.html',{'form':form,'answer':answer,'score':prediction_score})
	else:
		form = QuestionForm()
		return render(request,'main/index.html',{'form':form})

def history(request):
	q = Question.objects.all()
	return render(request,'main/history.html',{'questions':q})
