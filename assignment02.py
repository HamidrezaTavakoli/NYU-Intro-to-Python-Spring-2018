# <tag>content</tag>
def make_tag(tag,content):
    """returns a HTML tag."""
    return '<{}>{}</{}>'.format(tag,content,tag)

def odd_or_even(num):
    """returns whether a number is odd or even."""
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'

def sleeping_schedule(day):
    """returns whether the user can sleep in or not."""
    if day == 'saturday' or day == 'sunday':
        return 'It\'s the weekend. You can sleep in.'
    else:
        return 'It\'s not the weekend. Get out of the bed and go to work!.'

def main():
    tag = input('Enter the html tag you want to make:')
    content = input('Enter the content for the tag you want to make:')
    print(make_tag(tag,content))
    entered_num = input('Enter a number:')
    print('{} is {}'.format(entered_num,odd_or_even(int(entered_num))))
    day_of_week = input('What day is today? ')
    print(sleeping_schedule(day_of_week))


if __name__ == '__main__':
    main()
