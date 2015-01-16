---
layout: default
img: do_not_want
img_link: http://winterson.com/2005/06/episode-iii-backstroke-of-west.html
title: Syllabus
active_tab: syllabus
---

<table class="table table-striped"> 
  <tbody>
    <tr>
      <th>Date(s)</th>
      <th>Topic</th>
	  <th>Due</th>
      <th>Reading before Monday</th>
    </tr>
    {% for lecture in site.data.syllabus.past %}
    <tr>
      <td>{{ lecture.monday | date: "%b %d" }}&nbsp;{{ lecture.wednesday | date: "%b %d" }}</td>
      <td>
        {% if lecture.slides %}<a href="{{ lecture.slides }}">{{ lecture.title }}</a>
        {% else %}{{ lecture.title }}{% endif %}
      {% if lecture.links %}
        {% for link in lecture.links %}
          <p><a href="{{ link.url }}">{{ link.text }}</a></p>
        {% endfor %}
      {% endif %}
  {% if lecture.language %}
	<br/><a href="lin10.html">Language in 10</a>: <a href="{{ lecture.language_slides }}">{{ lecture.language }}</a>
        {% endif %}
      </td>
	  <td>
          {% if lecture.deadline %}
		  <ul class="fa-ul">
		  {% for deadline in lecture.deadline %}
		      <li> {% if deadline.url %}
                          <a href="{{ deadline.url }}">{{ deadline.title }}</a>
                      {% else %}
                          {{ deadline.title }} 
                      {% endif %}
                      ({{ deadline.day }})
	          </li>
      </td>
      <td>
        {% if lecture.reading %}
          <ul class="fa-ul">
          {% for reading in lecture.reading %}
            <li>
            {% if reading.optional %}<i class="fa-li fa fa-star"> </i>
            {% else %}<i class="fa-li fa"> </i> {% endif %}
            {{ reading.author }},
            {% if reading.url %}
            <a href="{{ reading.url }}">{{ reading.title }}</a>
            {% else %}
            {{ reading.title }} 
            {% endif %}
            </li>
          {% endfor %}
          </ul>
        {% endif %}
      </td>
    </tr>
    {% endfor %}

  </tbody>
</table>

