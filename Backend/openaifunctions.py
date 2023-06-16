import openai

openai.api_key = "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"

messages = []
messages = [{"role": "system", "content": 'I want you to act as a prompt engineer. You will help me write prompts for an ai art generator called Holara.I will provide you with short content ideas and your job is to elaborate these into full, explicit, coherent prompts. Prompts involve describing the content and style of images in concise accurate language. It is useful to be explicit and use references to popular culture, artists and mediums.Your focus needs to be on nouns and adjectives. I will give you some example prompts for your reference. Please define the exact camera that should be usedHere is a formula for you to use(content insert nouns here)(medium: insert artistic medium here)(style: insert references to genres, artists and popular culture here)(lighting, reference the lighting here)(colours reference color styles and palettes here)(composition: reference cameras, specific lenses, shot types and positional elements here) the most important part is when giving a prompt remove the brackets, speak in natural language and be more specific, use precise, articulate language. always output me two full prompt options that are different Example prompt: Portrait of a Celtic Jedi Sentinel with wet Shamrock Armor, green lightsaber, by Aleksi Briclot, shiny wet dramatic lighting.Always write the prompts following this example. '

'after generating the prompt, gather all the informations that i gave you and the informations from the prompt, use as inspiration to generate a detailed backstory and description for the character. '

'give me the answer like this: '

' prompt 1: '

' prompt 2: '

' Description: text (Do not break a line here, write everything on the same line!)'

'do not give any more words or phrases that arent from the prompt and description, also dont write prompt1, prompt2 at the start of the sentence!.'}]

def generate_stringinput(list2):
    list1 = ["Species:", "Sex/Gender:", "Age:", "Physical Shape:", "Hair Color:", "Eye Details:", "Main Colors:", "Deformation/Mark:", "Skills/Powers:", "Clothing:", "Context/Universe:", "Social/Context:", "Occupation/Profession:", "Ethnicity:", "Personality Traits:", "Artstyle / Art Inspiration:", "Extras:"]
    i = 0
    while i < len(list2):
        if list2[i] == '':
            if i < len(list2) and i < len(list1):
                list2.pop(i)
                list1.pop(i)
            else:
                break
        else:
            i += 1

    list3 = [f"{list1[i]} {list2[i]}" for i in range(len(list1))]
    str_list3 = '\n'.join(list3)
    return(str_list3)


def generate_prompts(list):
     message = generate_stringinput(list)
     print(message)
     messages.append({"role": "user", "content": message})
     response = openai.ChatCompletion.create(
         model="gpt-3.5-turbo",
        messages=messages)
     reply = response["choices"][0]["message"]["content"]
     messages.append({"role": "assistant", "content": reply})
     print("\n" + reply + "\n")
     print("")
     messages2 = reply.split('\n')
     i = 0
     while i < len(messages2):
      if messages2[i] == '':
        messages2.pop(i)
      else:
        i += 1
     return messages2