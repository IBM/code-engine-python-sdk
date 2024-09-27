# Create two new self-signed certificates using openssl
# The certs are used to verify TLS secret creations and updates
echo "Creating dummy certificates to verify TLS secrets ..."
openssl req -newkey ed25519 -nodes -keyout ./test/integration/domain.key -out ./test/integration/domain.csr -config ./test/integration/sample_cert.conf
openssl x509 -signkey test/integration/domain.key -in test/integration/domain.csr -req -days 365 -out test/integration/domain.crt
echo "Creating dummy certificates to verify TLS secrets [done]"
echo ""

# Create two private EC keys using openssl
# The SSH keys are used to verify SSH secret creations and updates
echo "Creating dummy SSH keys to verify SSH secrets ..."
openssl ecparam -name prime256v1 -genkey -noout -out ./test/integration/sshkey.pem
echo "Creating dummy certificates to verify SSH secrets [done]"
echo ""