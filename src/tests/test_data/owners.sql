INSERT INTO owners (name, email)
VALUES
{% for row in rows %}
    ('{{ row.name }}', '{{ row.email }}'){% if not loop.last %},{% endif %}
{% endfor %}

