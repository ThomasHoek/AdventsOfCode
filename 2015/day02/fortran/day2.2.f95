module day2module
   implicit none
contains
   !  https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort#Fortran
   SUBROUTINE Bubble_Sort(a)
      INTEGER, INTENT(in out), DIMENSION(:) :: a
      REAL :: temp
      INTEGER :: i, j
      LOGICAL :: swapped

      DO j = SIZE(a) - 1, 1, -1
         swapped = .FALSE.
         DO i = 1, j
            IF (a(i) > a(i + 1)) THEN
               temp = a(i)
               a(i) = a(i + 1)
               a(i + 1) = temp
               swapped = .TRUE.
            END IF
         END DO
         IF (.NOT. swapped) EXIT
      END DO
   END SUBROUTINE Bubble_Sort
end module day2module

program day2
   use day2module
   Use, intrinsic :: iso_fortran_env, Only: iostat_end
   implicit none

   INTEGER, DIMENSION(3) :: array
   INTEGER :: i, last_pointer = 1, counter, error, total = 0, val
   CHARACTER(len=10) :: input_text

   Open (10, file='..//input.txt')

   Do
      Read (10, *, iostat=error) input_text
      Select Case (error)
      Case (0)  ! reading went correct

         last_pointer = 1
         counter = 1
         do i = 1, len(TRIM(input_text))
            if (input_text(i:i) == 'x') then
               read (input_text(last_pointer:i - 1), '(i2)') val

               array(counter) = val
               last_pointer = i + 1
               counter = counter + 1
            end if
         end do

         read (input_text(last_pointer:i - 1), '(i2)') val
         array(3) = val
         CALL Bubble_Sort(array)
         total = total + PRODUCT(array) + array(1)*2 + array(2)*2

      Case (iostat_end) ! end of file
         Exit
      End Select
   End Do

   print *, total
end program day2
