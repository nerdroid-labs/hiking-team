from django.shortcuts import render
from app.models import Record, Photo
from hiking_team.settings import KAKAO_MAP_API_KEY
import json


def index(request):
    records = Record.objects.all()
    records = [(record.lat, record.lng, build_card(record)) for record in records]

    context = {'records': json.dumps(records), 'KAKAO_MAP_API_KEY':KAKAO_MAP_API_KEY}
    return render(request, 'index.html', context)


def build_card(record):
    mt_name = record.mountain_name
    participants = record.participants.values_list('name', flat=True)
    date = record.date
    photos = Photo.objects.filter(record=record)

    button_elements = []
    photo_elements = []
    for i, photo in enumerate(photos):
        button_element = f'<button type="button" class="carousel-btn" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="{i}" aria-label="Slide {i+1}"></button>'
        button_elements.append(button_element)

        photo_element = f'''
        <div class="carousel-item">
            <img loading="lazy" class="card-img" src="{photo.file.url}">
        </div>
        '''
        photo_elements.append(photo_element)

    button_elements = "\n".join(button_elements)
    photo_elements = "\n".join(photo_elements)

    card_element = f"""
    <div class="card">
      <ul class="list-group list-group-flush">
        <li class="list-group-item">
            <div class="row">
            <div class="col-8 mt-name"><b>{mt_name}</b></div>
            <div class="col-4" style="text-align: right;"><span class="close"><i class="far fa-window-close"></i></span></div>
            </div>
        </li>
        <li class="list-group-item p-0">
            <div id="{mt_name}" class="carousel slide text-center" data-bs-ride="carousel">
              <div class="carousel-indicators">
                {button_elements}
              </div>
              <div class="carousel-inner">
                {photo_elements}
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#{mt_name}" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#{mt_name}" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        </li>
        <li class="list-group-item">등반일: {date}</li>
        <li class="list-group-item">참가자: {", ".join(participants)}</li>
      </ul>
    </div>    
    """

    return card_element.strip()
