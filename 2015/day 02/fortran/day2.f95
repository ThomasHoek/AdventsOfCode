program day2
   Use, intrinsic :: iso_fortran_env, Only : iostat_end
   implicit none
   
   INTEGER :: i, last_pointer= 1, counter
   INTEGER :: error, total = 0
   INTEGER :: l, w, h, val
   CHARACTER(len=10) :: input_text
   CHARACTER(len=1) :: letter
   Open(10, file = '..//input.txt')
   
   Do
      Read( 10, *, iostat = error ) input_text
      Select Case( error )
      Case( 0 )  ! reading went correct
         
         last_pointer= 1
         counter = 1
         do i=1, len(TRIM(input_text))
            if (input_text(i:i) == 'x') then
               read(input_text(last_pointer:i-1),'(i2)') val

               select case(counter)
               case(1)
                  l = val
               case(2)
                  w = val
               end select
               
               last_pointer = i + 1
               counter = counter + 1
            end if
         end do
         read(input_text(last_pointer:i-1),'(i2)') val
         h = val
         
         total = total + (2*l*w + 2*w*h + 2*h*l) + min(l*w, w*h, h*l)


      Case( iostat_end ) ! end of file
         Exit
      End Select
   End Do
 
   print *, total
   
end program day2