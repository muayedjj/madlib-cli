# import re
#
# # Paths
#
# path_template = "../assets/mad_lips_template.txt"
# path_result = "../assets/mad_lips_result.txt"
#
# # Welcome Message
#
# wel_msg = """
#   *************************************************
#           Welcome to your custom Mad Libs!
#              Go wild with your answers.
#      Enter 'EXIT' or 'QUIT' to exit application.
#   *************************************************
#   """
#
#
# def welcome():
#     """
#     Prints welcome message at the beginning
#     """
#     print(wel_msg)
#
#
# result_message = """
#   *************************************************
#             Thank you for playing
# Here is your ML story, the result of your silliness ^^:
#   *************************************************
#   """
#
#
# # ML templates
#
#
# class MadLips:
#     def __init__(self, word_descriptions, template):
#         self.template = template
#         self.word_descriptions = word_descriptions
#
#
# # User Input
# """
# word_descriptions = [
#     "Adjective",
#     "A First Name",
#     "Past Tense Verb",
#     "Plural Noun",
#     "Large Animal",
#     "Small Animal",
#     "Number 1-50",
# ]
# """
#
#
# def get_user_input(word_descriptions):
#     words = []
#     print('please input words of the following types: ')
#     for desc in word_descriptions:
#         input_word = input(desc + " ")
#         words.append(input_word + " ")
#     return words
#
#
#
# def build_story(template, words):
#     story = template.format(*words)
#     return story
#
#
# with open(path_template, "r") as temp:
#     story_temp = temp.read()
#
# template = story_temp
# words = get_user_input(["noun", "verb"])
# story = build_story(template, words)
# print(story)
#
#


# ======================================================= Attempt 4

#
# import re
#
#
# def print_intro():
#     """Show intro and instructions to user."""
#     print(
#         """
#         #   *************************************************
#         #           Welcome to your custom Mad Libs!
#         #              Go wild with your answers.
#         #   *************************************************
#         #   """
#     )
#
#
# def read_template(template_filename):
#     """Get the template text from file and return as string."""
#     with open(template_filename, 'r') as infile:
#         return infile.read()
#
#
# def parse_template(template_text):
#     """Parse the template text. Return a list of user prompts and the template text with the prompts stripped out."""
#     pattern = '\{(.*?)\}'
#     prompts = re.findall(pattern, template_text)
#     template_text = re.sub(pattern, '{}', template_text)
#     return template_text, prompts
#
#
# def get_user_responses(prompts):
#     """Go through the list of prompts and record user's answers. Return the answers in a list."""
#     responses = []
#     for prompt in prompts:
#         responses.append(input(f'Enter a {prompt.lower()}: '))
#     return responses
#
#
# def merge(template_text, responses):
#     """Replace the text blanks with the user's responses. Return the string."""
#     return template_text.format(*responses)
#
#
# def print_formatted_text(template_text):
#     """Print out the final text."""
#     print(template_text)
#
#
# def write_to_file(filename, template_text):
#     """Open a file for writing and write the template_text into it."""
#     with open(filename, 'w') as out_file:
#         out_file.write(template_text)
#
#
# def run():
#     """Enter script execution."""
#     print_intro()
#     filename = '../assets/mad_lips_template.txt'
#     template_text = read_template(filename)
#     template_text, prompts = parse_template(template_text)
#     responses = get_user_responses(prompts)
#     template_text = merge(template_text, responses)
#     print_formatted_text(template_text)
#     out_filename = '../assets/mad_lips_result.txt'
#     write_to_file(out_filename, template_text)
#
#
# if __name__ == '__main__':
#     run()
print('The code is NOT ready')