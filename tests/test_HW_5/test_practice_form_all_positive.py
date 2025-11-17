from pathlib import Path

from selene import browser, by, have, command


def test_practice_form_all_positive():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Инна')
    browser.element('#lastName').type('Тюляева')
    browser.element('#userEmail').type('tyulyaeva.inna@admin.ru')
    browser.element(by.text('Female')).click()
    browser.element('#userNumber').type('9178332203')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('July')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1991')).click()
    browser.element('.react-datepicker__day--020:not(.react-datepicker__day--outside-month').click()
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('#hobbiesWrapper').element(by.text('Reading')).click()
    picture = str(Path(__file__).parent.parent.joinpath('resources', 'test_inna.png').resolve())
    browser.element('#uploadPicture').set_value(picture)
    browser.element('#currentAddress').type('Санкт-Петербург, п. Парглово')
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Agra').press_enter()

    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.modal-content table tbody tr td:nth-child(2)').should(have.exact_texts(
        'Инна Тюляева',
        'tyulyaeva.inna@admin.ru',
        'Female',
        '9178332203',
        '20 July,1991',
        'Arts',
        'Reading',
        'test_inna.png',
        'Санкт-Петербург, п. Парглово',
        'Uttar Pradesh Agra'
    ))