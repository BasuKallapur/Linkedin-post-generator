from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "1 to 10 lines"
    elif length == "Medium":
        return "10 to 20 lines"
    else:
        return "20 to 35 lines"


def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content

    # tuning the prompt to get desired outcome
def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    - If Language is Hinglish, it means a mix of Hindi and English. However, ensure the script is written in English.
    4) Structure the content into multiple paragraphs, with each paragraph containing 3-4 sentences for better readability.
    5) Add relevant and popular hashtags at the end.
    6) Maintain a professional tone suitable for LinkedIn's audience, making the content engaging and informative.
    7) Use relevant emojis to enhance engagement and readability. For example, use emojis like 🚀 for excitement, 🤔 for thought-provoking content, or 🎉 for celebratory posts.

    '''
    # prompt = prompt.format(post_topic=tag, post_length=length_str, post_language=language)

    examples = few_shot.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: # Use max two samples
            break

    return prompt


if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health"))