from setuptools import setup

setup(name='pi_local_mqtt_client',
      version='0.1',
      description='Python scripts that publish local information via mqtt, e.g. cpu temperature and room temperature via a i2c sensor.',
      url='https://github.com/Cakem1x/pi_local_mqtt_client',
      author='Matthias Holoch',
      author_email='mholoch@gmail.com',
      scripts=['pi_local_mqtt_client/bin/client'],
      zip_safe=False)
