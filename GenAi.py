from ollama import chat



def getsummary(fileContents,type):
    cmd="Summarise the following :"+type+"way+\n"+fileContents;
    msg=[
    {'role':'user',
     "content":cmd}


    ]
    response=chat("llama2",messages=msg)
    print(response["message"]["content"])