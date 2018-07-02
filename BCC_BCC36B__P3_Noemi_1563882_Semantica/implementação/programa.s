	.text
	.file	"programa.ll"
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2               # -- Begin function main
.LCPI0_0:
	.long	1065353216              # float 1
	.text
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:                                 # %entry
	movl	$10, global.a(%rip)
	xorl	%eax, %eax
	testb	%al, %al
	jne	.LBB0_2
# BB#1:                                 # %entao
	movl	$1, -4(%rsp)
	jmp	.LBB0_3
.LBB0_2:                                # %senao
	movl	$0, -4(%rsp)
.LBB0_3:                                # %fim
	cvtsi2ssl	-4(%rsp), %xmm0
	cvttss2si	%xmm0, %eax
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function

	.section	".note.GNU-stack","",@progbits
