Feature: Testing site cbr.ru
Scenario: Search Bank of Russia site on google.ru
  Given website www.google.ru
  When push search button with text 'Центральный банк РФ'
  Then displayed page www.google.ru and opened cbr.ru site link 
  Then check the opening of the site cbr.ru
  Then on cbr.ru opened link Internet-reception
  Then opened link Write gratitude
  Then write in textarea MessageBody 'случайный текст'
  Then select the checkbox Agreement
  Then make screenshot and send email
  Then press the button Three strips
  Then clicked on the section About
  Then clicked link Warning
  Then save warning text
  Then changed page language to en
  Then check warning text is different from the memorized text previously
  Then make screenshot and send email
  