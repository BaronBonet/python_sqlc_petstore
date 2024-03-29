FROM flyway/flyway:10.10-alpine

WORKDIR /flyway

COPY scripts/migrate.sh ./

COPY migrations ./migrations/

ENTRYPOINT ["./migrate.sh"]

