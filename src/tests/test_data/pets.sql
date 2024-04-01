INSERT INTO pets (id, name, species, breed, age, owner_id, created_at)
VALUES
{% for row in rows %}
    ({{ row.id }}, '{{ row.name }}', '{{ row.species }}', '{{ row.breed }}', {{ row.age }}, {{ row.owner_id }}, '{{ row.created_at.isoformat() }}'){% if not loop.last %},{% endif %}
{% endfor %}
