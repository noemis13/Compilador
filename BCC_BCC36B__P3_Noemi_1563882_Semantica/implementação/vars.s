	.text
	.file	"vars.ll"
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2               # -- Begin function main
.LCPI0_0:
	.long	1092616192              # float 10
	.text
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:                                 # %entry
	movl	$0, -8(%rsp)
	movl	$1065353216, -12(%rsp)  # imm = 0x3F800000
	movl	$10, g(%rip)
	movl	$1092616192, h(%rip)    # imm = 0x41200000
	movl	$11, -4(%rsp)
	movss	-12(%rsp), %xmm0        # xmm0 = mem[0],zero,zero,zero
	addss	.LCPI0_0(%rip), %xmm0
	movss	%xmm0, -12(%rsp)
	movl	-8(%rsp), %eax
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	g,@object               # @g
	.comm	g,4,4
	.type	h,@object               # @h
	.comm	h,4,4

	.section	".note.GNU-stack","",@progbits
