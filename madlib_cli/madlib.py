import re


def print_intro():
    """Show welcome message to user."""
    print(
        """
        #   *************************************************
        #           Welcome to your custom Mad Libs!
        #              Go wild with your answers.
        #   *************************************************
        #   """
    )


def read_template(template_filename):
    """Get the template text from file and return as string."""
    try:
        with open(template_filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(template_text):
    """Parse the template text.
    Return a list of user prompts and the template text with the prompts stripped out."""
    pattern = r'\{(.*?)\}'
    prompts = re.findall(pattern, template_text)
    template_text = re.sub(pattern, '{}', template_text)
    # print(prompts)
    # print(template_text)
    return template_text, tuple(prompts)


def get_user_responses(prompts):
    """Go through the list of prompts and record user's answers. Return the answers in a list."""
    responses = []
    for prompt in prompts:
        responses.append(input(f'Enter a {prompt.lower()}: '))
    return responses


def merge(template_text, responses):
    """Replace the text blanks with the user's responses. Return the string."""
    return template_text.format(*responses)


def print_formatted_text(template_text):
    """Print out the final text."""
    print(template_text)


def write_to_file(filename, template_text):
    """Open a file for writing and write the template_text into it."""
    with open(filename, 'w') as out_file:
        out_file.write(template_text)


def run():
    """Enter script execution."""
    print_intro()
    filename = '../assets/mad_lips_template.txt'
    template_text = read_template(filename)
    template_text, prompts = parse_template(template_text)
    responses = get_user_responses(prompts)
    template_text = merge(template_text, responses)
    # print(template_text)
    print_formatted_text(template_text)
    out_filename = '../assets/mad_lips_result.txt'
    write_to_file(out_filename, template_text)


if __name__ == '__main__':
    run()
