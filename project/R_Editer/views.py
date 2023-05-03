from .forms import StudentForm
from django.shortcuts import render

# Create your views here.


def home(request):
    form = StudentForm
    mydict = {
        'form' : form 
    }
    return render(request,'home.html', context=mydict)

def login(request):
    return render(request, 'login.html')






 # RoBERTa doesn’t have token_type_ids, you don’t need to indicate which token belongs to which segment. Just separate your segments with the separation token tokenizer.sep_token (or </s>)



# Manually added by Sakshi 
# https://huggingface.co/transformers/v2.11.0/_modules/transformers/modeling_roberta.html#RobertaForMaskedLM
# https://huggingface.co/transformers/v2.11.0/model_doc/roberta.html#robertaformaskedlm
# https://huggingface.co/roberta-base
#from django.http import JsonResponse
#from transformers import pipeline, RobertaTokenizer, RobertaForMaskedLM

#Load pretrained Roberta model and tokenizer
#model_name = 'roberta-base'  #Replace with the desired Roberta Model name
#tokenizer = RobertaTokenizer.from_pretrained(model_name)
#model = RobertaForMaskedLM.from_pretrained(model_name)

#def autocomplete(request):
 #   text = request.GET.get('text', '')

    #Tokenize input text
  #  input_ids = tokenizer.encode(text, return_tensors='pt')

    #Generate suggestions using RoBERTa
   # suggestions = []
   # if input_ids.nume1() > 0:
    #    masked_inout_ids = input_ids.clone()
     #   masked_inout_ids[input_ids != tokenizer.mask_token_id] = tokenizer.mask_token_id
        # incomplete                            