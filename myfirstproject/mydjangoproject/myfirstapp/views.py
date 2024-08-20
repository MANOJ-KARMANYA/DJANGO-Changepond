from django.shortcuts import render

# Mock data
cards_data = [
    {'id': 1, 'card_title': 'Exploring Advancements in AI', 'card_description': '"Tech Day was an incredible experience! The hands-on sessions with the latest gadgets and software were both informative and engaging. The keynote speeches provided valuable insights into the future of technology and innovation. A big thanks to the organizers for a well-executed event!"', 'image': 'https://media.licdn.com/dms/image/C5622AQEbtRF91elgzg/feedshare-shrink_800/0/1620724490609?e=2147483647&v=beta&t=qb3FnvO_wDT7YUTKs6OB0eioLagXjslkjT4X8QCaaBs'},
    {'id': 2, 'card_title': 'AI is Transforming Technology', 'card_description': "The advancements in AI showcased at the event were truly impressive. From natural language processing to sophisticated machine learning algorithms, the potential applications are vast and exciting. It’s fascinating to see how AI is evolving to tackle complex problems and enhance everyday experiences.", 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY1YFrTrAc8ikRiMEwHBc0kdxgUtrh34mJc2vbFONdPiwNZmKfrd6jw2FaS-GUX8tXUfY&usqp=CAU'},
    {'id': 3, 'card_title': 'Integrating AI with the Metaverse', 'card_description': "The presentations on the metaverse were eye-opening. It’s amazing to see how virtual environments are becoming more immersive and interactive. The potential for the metaverse to revolutionize social interactions, work environments, and entertainment is immense. I’m eager to see how these developments unfold.", 'image': 'https://digitalscholar.in/wp-content/uploads/2022/06/National-Technology-Day-Social-Media-Post-Ideas.png'},
]

def land_page(request):

    section_name = 'My First Django Project'
    return render(request, 'cardsdetail/index.html', {'section_name': section_name, 'cards': cards_data})

def second_page(request):
    return render(request, 'includes/cards.html', {'cards': cards_data})

def detail_page(request, card_id):
    for c in cards_data:
        if c['id'] == int(card_id):
            card = c
    return render(request, 'cardsdetail/detail.html', {'card': card})