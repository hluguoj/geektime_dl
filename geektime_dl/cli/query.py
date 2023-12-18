# coding=utf8

import sys

from geektime_dl.cli import Command


_course_map = {
    '1': '专栏', '2': '微课', '3': '视频', '4': '其他'
}


class Query(Command):
    """查看课程列表"""

    def run(self, cfg: dict):

        dc = self.get_data_client(cfg)

        data = dc.get_course_list()

        result_str = ''
        columns = data['products']
        result_str += "\t{:<12}{}\t{}\t{:<10}\t{}\n".format(
            '课程ID', '已订阅', '已完结', '课程标题', '视频课')
        for c in columns:
            is_finished = self.is_course_finished(c)
            result_str += "\t{:<15}{}\t{}\t{:<10}\t{}\n".format(
                str(c['id']),
                '是' ,
                '是' if is_finished else '否',
                c['title'],
                '是' if c['is_video'] else '否',

            )

        sys.stdout.write(result_str)
        return result_str

