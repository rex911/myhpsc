
program test2

    use quadrature_omp, only: trapezoid, error_table

    implicit none
    real(kind=8) :: a,b,int_true
    integer :: nvals(32), i

    a = 0.d0
    b = 2.d0
    int_true = (b-a) + (b**4 - a**4) / 4.d0 - (cos(1000*b) - cos(1000*a))/1000.d0

    print 10, int_true
 10 format("true integral: ", es22.14)
    print *, " "  ! blank line

    ! values of n to test:
    do i=1,32
        nvals(i) = 5 * 2**(i-1)
        enddo

    call error_table(f, a, b, nvals, int_true)

contains

    real(kind=8) function f(x)
        implicit none
        real(kind=8), intent(in) :: x 
        
        f = 1.d0 + x**3 + sin(1000*x)
    end function f

end program test2
