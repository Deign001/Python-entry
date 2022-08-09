import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###
text = input("Are you a coding Wizard :")
source_language_code = input("I can take you: ")
target_language_code = input("I bet you are: ") 

def main():
    translate_text(
        Text=text,
        SourceLanguageCode="en",
        TargetLanguageCode="fr"
        )

if __name__=="__main__":
    main()