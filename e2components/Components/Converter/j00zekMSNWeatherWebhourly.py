from __future__ import absolute_import #zmiana strategii ladowanie modulow w py2 z relative na absolute jak w py3
try:
    from Components.Converter.MSNWeatherWebhourly import MSNWeatherWebhourly as j00zekMSNWeatherWebhourly
except Exception:
    from Components.Converter.j00zekMissingConverter import j00zekMissingConverter as j00zekMSNWeatherWebhourly
