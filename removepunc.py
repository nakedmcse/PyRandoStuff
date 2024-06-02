# Remove Punctuation
input = "Amy said, \"The cake is ready, let's eat!!\""
punctuation = "!()-[]{};:'\",<>./?@#$%^&*_~! "
nopunctuation = str.maketrans('', '', punctuation)
print(input.translate(nopunctuation))