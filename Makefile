generate:
	@sqlc generate -f src/adapters/postgres_repository/sqlc.yaml

clean:
	@rm -rf */__pycache__ */pytest_cache */.pytest_cache */.coverage */.coverage.*
