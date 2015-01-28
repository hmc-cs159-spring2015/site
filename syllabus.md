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
      <td>
	    {% if lecture.mondayslides %}
		  <a href="{{ lecture.mondayslides }}">{{ lecture.monday | date: "%b %d"}}</a>
        {% else %}  {{ lecture.monday | date: "%b %d" }}{% endif %}
        <br/>
        {% if lecture.wednesdayslides %}
		  <a href="{{ lecture.wednesdayslides }}">{{ lecture.wednesday | date: "%b %d"}}</a>
        {% else %}  {{ lecture.wednesday | date: "%b %d" }}{% endif %}
	  </td>
      <td>
        {{ lecture.title }}
      {% if lecture.links %}
        {% for link in lecture.links %}
          <p><a href="{{ link.url }}">{{ link.text }}</a></p>
        {% endfor %}
      {% endif %}
  {% if lecture.mondaylanguage %}
	<br/><a href="lin10.html">Pres.</a>: <a href="{{ lecture.mondaylanguage_slides }}">{{ lecture.mondaylanguage }}</a>
        {% endif %}
  {% if lecture.wednesdaylanguage %}
	<br/><a href="lin10.html">Pres.</a>: <a href="{{ lecture.wednesdaylanguage_slides }}">{{ lecture.wednesdaylanguage }}</a>
        {% endif %}
      </td>
	  <td>
	      {% if lecture.preview %}
	          <a href="hw{{ lecture.preview}}.html">PReview {{lecture.preview}}</a>
              <br/>
		  {% endif %}
		  {% if lecture.projectnumber %}
	          <a href="project{{ lecture.projectnumber}}.html">{{lecture.projecttitle}}&nbsp;Project</a>
          {% endif %}
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

