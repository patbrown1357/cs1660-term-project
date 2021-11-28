FROM sonarqube:9.2.0-community
ENV PATH "$PATH:/bin/lib/sonar-scanner-4.6.2.2472-linux/bin"
COPY sonar-scanner-cli/ /bin/lib/
RUN ["dos2unix", "/bin/lib/sonar-scanner-4.6.2.2472-linux/bin/sonar-scanner"]