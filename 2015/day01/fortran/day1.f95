program day1
    implicit none
    INTEGER :: i, left=0, right=0
    CHARACTER(len=10000) :: input_text

    ! https://stackoverflow.com/questions/54399425/how-to-know-that-we-reached-eof-in-fortran-77
    Open(10, file = '..//input.txt')
    Read( 10, *) input_text
    
    do i =1, LEN(TRIM(input_text))
        ! print *, input_text(i:i)
        if (input_text(i:i) .EQ. '(') then
            left = left + 1
        else
            right = right + 1
        endif
    end do
    print *,  left - right
    
end program day1