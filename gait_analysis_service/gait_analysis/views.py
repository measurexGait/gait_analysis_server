# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.http import HttpResponse
from gait_analysis_service.gait_analysis.models import *
from gait_analysis_service.user_management.models import *
import simplejson
import math
import time


def data_upload(req):
    try:
        # 将json数据转化为python数据格式
        data = simplejson.loads(req.body)

        # 通过令牌从数据库获取用户
        user = User.objects.get(last_name=data['token'])
        sta_index = Sta_index(user_id=user, device_id=data['device_id'])
        sta_index.save()
        if 'signal' in data['data']:
            # 创建空的singles list，
            signals = []
            # 从data中获取一系列singal中的数据
            for tmp in data['data']['signal']:
                # 创建一个model中的Single对象
                signal = Signal_info()
                # 将signal数据写入
                signal.signal_strength = tmp['signal_strength']
                # 将时间戳写入
                signal.timestamp = tmp['timestamp']
                # 将这个对象追加到singles list中
                signals.append(signal)
                # 批量创建对象，导入大量数据，提升性能，避免逐条插入
            Signal_info.objects.bulk_create(signals)

        if 'pressure_l_foot' in data['data']:
            # 创建空的pressures list
            pressures_l_foot = []
            # 从data中获取一系列pressures中的数据
            for tmp in data['data']['pressure_l_foot']:
                # 创建一个model中的pressures对象
                pressure_l_foot = Pressure_l_foot()
                # 将user数据写入，对应每个用户的压力
                pressure_l_foot.user = user
                # 将device_id数据写入，对应每个设备的id
                pressure_l_foot.device_id = data['device_id']
                # 将时间戳写入
                pressure_l_foot.timestamp = tmp['timestamp']
                # 将不同pressure传感器的数据写入
                pressure_l_foot.pre_l_a = tmp['a']
                pressure_l_foot.pre_l_b = tmp['b']
                pressure_l_foot.pre_l_c = tmp['c']
                pressure_l_foot.pre_l_d = tmp['d']
                # 将索引写入
                pressure_l_foot.index_id = sta_index.sta_index
                # 将这个对象追加到pressures list中
                pressures_l_foot.append(pressure_l_foot)
            # 批量创建对象，导入大量数据，提升性能，避免逐条插入
            Pressure_l_foot.objects.bulk_create(pressures_l_foot)

        if 'pressure_r_foot' in data['data']:
            # 创建空的pressures list
            pressures_r_foot = []
            # 从data中获取一系列pressures中的数据
            for tmp in data['data']['pressure_r_foot']:
                # 创建一个model中的pressures对象
                pressure_r_foot = Pressure_r_foot()
                # 将user数据写入，对应每个用户的压力
                pressure_r_foot.user = user
                # 将device_id数据写入，对应每个设备的id
                pressure_r_foot.device_id = data['device_id']
                # 将时间戳写入
                pressure_r_foot.timestamp = tmp['timestamp']
                # 将不同pressure传感器的数据写入
                pressure_r_foot.pre_r_a = tmp['a']
                pressure_r_foot.pre_r_b = tmp['b']
                pressure_r_foot.pre_r_c = tmp['c']
                pressure_r_foot.pre_r_d = tmp['d']
                # 将索引写入
                pressure_r_foot.index_id = sta_index.sta_index
                # 将这个对象追加到pressures list中
                pressures_r_foot.append(pressure_r_foot)
            # 批量创建对象，导入大量数据，提升性能，避免逐条插入
            Pressure_r_foot.objects.bulk_create(pressures_r_foot)


        if 'acceleration_l_foot' in data['data']:
            # 创建空的accelerations list
            accelerations_l_foot = []
            # 从data中获取一系列acceleration中的数据
            for tmp in data['data']['acceleration_l_foot']:
                # 创建一个model中的Acceleration对象
                acceleration_l_foot = Acceleration_l_foot()
                # 将user数据写入，对应每个用户的Acceleration
                acceleration_l_foot.user = user
                # 将device_id数据写入，对应每个设备的id
                acceleration_l_foot.device_id = data['device_id']
                # 将时间戳写入
                acceleration_l_foot.timestamp = tmp['timestamp']
                # 将不同acceleration传感器的数据写入
                acceleration_l_foot.acc_l_x = tmp['x']
                acceleration_l_foot.acc_l_y = tmp['y']
                acceleration_l_foot.acc_l_z = tmp['z']
                # 将索引写入
                acceleration_l_foot.index_id = sta_index.sta_index
                # 将这个对象追加到acceleration list中
                accelerations_l_foot.append(acceleration_l_foot)
            # 批量创建对象，导入大量数据，提升性能，避免逐条插入
            Acceleration_l_foot.objects.bulk_create(accelerations_l_foot)

        if 'acceleration_r_foot' in data['data']:
            # 创建空的accelerations list
            accelerations_r_foot = []
            # 从data中获取一系列acceleration中的数据
            for tmp in data['data']['acceleration_r_foot']:
                # 创建一个model中的Acceleration对象
                acceleration_r_foot = Acceleration_r_foot()
                # 将user数据写入，对应每个用户的Acceleration
                acceleration_r_foot.user = user
                # 将device_id数据写入，对应每个设备的id
                acceleration_r_foot.device_id = data['device_id']
                # 将时间戳写入
                acceleration_r_foot.timestamp = tmp['timestamp']
                # 将不同acceleration传感器的数据写入
                acceleration_r_foot.acc_r_x = tmp['x']
                acceleration_r_foot.acc_r_y = tmp['y']
                acceleration_r_foot.acc_r_z = tmp['z']
                # 将索引写入
                acceleration_r_foot.index_id = sta_index.sta_index
                # 将这个对象追加到acceleration list中
                accelerations_r_foot.append(acceleration_r_foot)
            # 批量创建对象，导入大量数据，提升性能，避免逐条插入
            Acceleration_r_foot.objects.bulk_create(accelerations_r_foot)


        if 'gyroscope_l_foot' in data['data']:
            # 创建空的gyroscope list
            gyroscopes_l_foot = []
            # 从data中获取一系列gyroscope中的数据
            for tmp in data['data']['gyroscope_l_foot']:
                # 创建一个model中的gyroscope对象
                gyroscope_l_foot = Gyroscope_l_foot()
                # 将user数据写入，对应每个用户的gyroscope
                gyroscope_l_foot.user = user
                # 将device_id数据写入，对应每个设备的id
                gyroscope_l_foot.device_id = data['device_id']
                # 将时间戳写入
                gyroscope_l_foot.timestamp = tmp['timestamp']
                # 将不同gyroscope传感器的数据写入
                gyroscope_l_foot.gyro_l_x = tmp['x']
                gyroscope_l_foot.gyro_l_y = tmp['y']
                gyroscope_l_foot.gyro_l_z = tmp['z']
                # 将索引写入
                gyroscope_l_foot.index_id = sta_index.sta_index
                # 将这个对象追加到gyroscope list中
                gyroscopes_l_foot.append(gyroscope_l_foot)
                # 批量创建对象，导入大量数据，提升性能，避免逐条插入
            Gyroscope_l_foot.objects.bulk_create(gyroscopes_l_foot)

        if 'gyroscope_r_foot' in data['data']:
            # 创建空的gyroscope list
            gyroscopes_r_foot = []
            # 从data中获取一系列gyroscope中的数据
            for tmp in data['data']['gyroscope_r_foot']:
                # 创建一个model中的gyroscope对象
                gyroscope_r_foot = Gyroscope_r_foot()
                # 将user数据写入，对应每个用户的gyroscope
                gyroscope_r_foot.user = user
                # 将device_id数据写入，对应每个设备的id
                gyroscope_r_foot.device_id = data['device_id']
                # 将时间戳写入
                gyroscope_r_foot.timestamp = tmp['timestamp']
                # 将不同gyroscope传感器的数据写入
                gyroscope_r_foot.gyro_r_x = tmp['x']
                gyroscope_r_foot.gyro_r_y = tmp['y']
                gyroscope_r_foot.gyro_r_z = tmp['z']
                # 将索引写入
                gyroscope_r_foot.index_id = sta_index.sta_index
                # 将这个对象追加到gyroscope list中
                gyroscopes_r_foot.append(gyroscope_r_foot)
                # 批量创建对象，导入大量数据，提升性能，避免逐条插入
            Gyroscope_r_foot.objects.bulk_create(gyroscopes_r_foot)

        # 构建一个表示成功的dict
        result = {
            'successful': True,
            'error': {
                'id': '',
                'message': ''
            }
        }

    # 捕获异常
    except Exception as e:
        Sta_index.objects.get(sta_index=sta_index.sta_index).delete()
        result = {
            'successful': False,
            'error': {
                'id': '1024',
                'message': e.args
            }
        }
    finally:
        return HttpResponse(simplejson.dumps(result), content_type="application/json")


def calculate(request):
    data = simplejson.loads(request.body)
    index_id = data['index_id']

    pressure_l_foot = Pressure_l_foot.object.filter(index_id=index_id)
    pressure_r_foot = Pressure_r_foot.object.filter(index_id=index_id)
    acceleration_l_foot = Acceleration_l_foot.object.filter(index_id=index_id)
    acceleration_r_foot = Acceleration_r_foot.object.filter(index_id=index_id)
    gyroscope_l_foot = Gyroscope_l_foot.object.filter(index_id=index_id)
    gyroscope_r_foot = Gyroscope_r_foot.object.filter(index_id=index_id)

    start_time = Pressure_l_foot.object.filter(index_id=index_id).value('timestamp')[0]
    end_time = Pressure_l_foot.object.filter(index_id=index_id).value('timestamp')[-1]

    flag = False
    fl = False
    steps = 0
    threshold = 80
    max_velocity = 0
    velocity = 0
    distance = 0
    stance_time = 0
    swing_time = 0
    stance = 0
    swing = 0
    angle = 0
    trace_x_list = []
    trace_y_list = []
    velocity_list = []
    for i in range(len(pressure_l_foot)):
        p_l = int(pressure_l_foot.a[i])+int(pressure_l_foot.b[i])+int(pressure_l_foot.c[i])+int(pressure_l_foot.d[i])
        p_r = int(pressure_r_foot.a[i])+int(pressure_r_foot.b[i])+int(pressure_r_foot.c[i])+int(pressure_r_foot.d[i])

        if p_l < threshold:
            if flag is False:
                flag = True
            elif stance != 0:
                swing = pressure_l_foot.timestamp[i]
                stance_time = swing-stance
                angle += float(gyroscope_l_foot.x[i])*2000/32768/180*math.pi*0.02
                velocity += 0.02 * float(acceleration_l_foot.x[i])*16/32768
                if velocity > 0:
                    velocity = 0
                elif velocity < max_velocity:
                    max_velocity = velocity
                distance += 0.02*abs(velocity)
                fl = False
                if p_r < threshold:
                    pass
                else:
                    pass
        elif p_l >= threshold:
            if flag is True and fl is False:
                stance = pressure_l_foot.timestamp[i]
                steps += 1
                fl = True
                if swing != 0:
                    swing_time = stance-swing
                trace_x_list.append(swing_time*abs(velocity)*math.cos(angle))
                trace_y_list.append(swing_time*abs(velocity)*math.sin(angle))
                velocity_list.append(velocity)
                swing = 0
                velocity = 0
                angle = 0
                if p_r < threshold:
                    pass
                else:
                    pass

    cadence = steps/(pressure_l_foot.timestamp[-1]-pressure_l_foot.timestamp[0])*60000
    velocity = distance/(end_time-start_time)*1000
    double_s_time = 0
    acceleration_time = 0
    deceleration_time = 0
    l_step_length = 0
    r_step_length = 0
    statistics_info = Statistics_info(index_id=index_id, start_time=start_time, end_time=end_time, steps=steps,
                                      velocity=velocity, velocity_max=max_velocity, distance=distance,
                                      l_step_length=l_step_length, r_step_length=r_step_length, cadence=cadence,
                                      stance_time=stance_time, swing_time=swing_time, a_time=acceleration_time,
                                      d_time=deceleration_time, d_s_time=double_s_time)
    statistics_info.save()
    resultList = []
    for tmp in range(len(trace_x_list)):
        trace = Trace_info(index_id=index_id, x=trace_x_list[i], y=trace_y_list[i], v=velocity_list[i])
        resultList.append(trace)
    Trace_info.objects.bulk_create(resultList)


def main_page(request):
    try:
        if request.user.is_authenticated():
            return render_to_response('gaitanalysis/main.html', RequestContext(request))
    except Exception as e:
        response = HttpResponse()
        response.write("<script>alert('请先登录'),window.location.href='/homepage/index/'</script>")
        return response


def main_query(request):
    try:
        if request.user.is_authenticated():
            if request.method == "GET":
                start_time = int(request.GET['start_time'])
                end_time = int(request.GET['end_time'])

                sta_index = Sta_index.objects.filter(user_id=request.user).order_by('-sta_index')

                duration = 0
                calorie = 0
                steps = 0
                categoriesList = []
                stepsList = []
                calorieList = []
                durationList = []
                for tmp in sta_index:
                    statistics = Statistics_info.objects.get(index_id=tmp.sta_index)
                    if statistics.start_time <= end_time:
                        if statistics.start_time >= start_time:
                            categoriesList.append(statistics.start_time)
                            stepsList.append(statistics.steps)
                            calorieList.append(statistics.calorie)
                            durationList.append(statistics.end_time - statistics.start_time)

                            duration += statistics.end_time - statistics.start_time
                            calorie += statistics.calorie
                            steps += statistics.steps
                        else:
                            w_summary = {
                                'duration': duration,
                                'calorie': calorie,
                                'steps': steps
                            }
                            graph = {
                                'categoriesList': categoriesList,
                                'stepsList': stepsList,
                                'calorieList': calorieList,
                                'durationList': durationList
                            }
                            result = {
                                'w_summary': w_summary,
                                'graph': graph
                            }
                            return HttpResponse(simplejson.dumps(result), content_type='application/json')
                w_summary = {
                    'duration': duration,
                    'calorie': calorie,
                    'steps': steps
                }
                graph = {
                    'categoriesList': categoriesList,
                    'stepsList': stepsList,
                    'calorieList': calorieList,
                    'durationList': durationList
                }
                result = {
                    'w_summary': w_summary,
                    'graph': graph
                }
                return HttpResponse(simplejson.dumps(result), content_type='application/json')
    except Exception as e:
        response = HttpResponse()
        response.write("<script>alert('error'),window.location.href='/homepage/index/'</script>")
        return response


def record_query(request):
    try:
        if request.user.is_authenticated():
            if request.method == "GET":
                start_time = int(request.GET['start_time'])
                end_time = int(request.GET['end_time'])

                sta_index = Sta_index.objects.filter(user_id=request.user).order_by('-sta_index')
                resultList = []
                for tmp in sta_index:
                    statistics = Statistics_info.objects.get(index_id=tmp.sta_index)
                    if statistics.start_time <= end_time:
                        if statistics.start_time >= start_time:
                            s_time = time.strftime("%Y-%m-%d %H:%M", time.localtime(statistics.start_time/1000))
                            duration = statistics.end_time - statistics.start_time
                            resultList.append({"start_time": s_time, "steps": statistics.steps,
                                               "calorie": statistics.calorie, "duration": duration})
                        else:
                            return HttpResponse(simplejson.dumps(resultList), content_type='application/json')
                return HttpResponse(simplejson.dumps(resultList), content_type='application/json')
    except Exception as e:
        response = HttpResponse()
        response.write("<script>alert('error'),window.location.href='/homepage/index/'</script>")
        return response


def detail(request):
    try:
        if request.user.is_authenticated():
            if request.method == "POST":
                statistics = Statistics_info.objects.filter(start_time=request.POST['date'])
                for tmp in statistics:
                    index_id = tmp.index_id
                    steps = tmp.steps
                    v = tmp.velocity
                    max_v = tmp.velocity_max
                    s = tmp.distance
                    sl = tmp.l_step_length
                    sr = tmp.r_step_length
                    cadence = tmp.cadence
                    stance_time = tmp.stance_time
                    swing_time = tmp.swing_time
                    a_time = tmp.acceleration_time
                    d_time = tmp.deceleration_time
                    d_s_time = tmp.double_s_time
                    calorie = tmp.calorie
                index_id = "%s" % index_id

                l_pressure = Pressure_l_foot.objects.filter(index_id=index_id)
                r_pressure = Pressure_r_foot.objects.filter(index_id=index_id)
                l_acceleration = Acceleration_l_foot.objects.filter(index_id=index_id)
                r_acceleration = Acceleration_r_foot.objects.filter(index_id=index_id)
                l_gyroscope = Gyroscope_l_foot.objects.filter(index_id=index_id)
                r_gyroscope = Gyroscope_r_foot.objects.filter(index_id=index_id)
                trace = Trace_info.objects.filter(index_id=index_id)

                w_summary = {
                    "steps": steps,
                    "v": v,
                    "max_v": max_v,
                    "s": s,
                    "sl": sl,
                    "sr": sr,
                    "stance_time": stance_time,
                    "swing_time": swing_time,
                    "cadence": cadence,
                    "a_time": a_time,
                    "d_time": d_time,
                    "d_s_time": d_s_time,
                    "calorie": calorie
                }

                plotLines = [0.1, 1, 2]

                l_a = []
                l_b = []
                l_c = []
                l_d = []
                categories = []
                l_accx = []
                l_accy = []
                l_accz = []
                l_gyrox = []
                l_gyroy = []
                l_gyroz = []
                xList = []
                yList = []
                vList = []

                for tmp in l_pressure:
                    l_a.append(tmp.pre_l_a)
                    l_b.append(tmp.pre_l_b)
                    l_c.append(tmp.pre_l_c)
                    l_d.append(tmp.pre_l_d)
                    categories.append(tmp.timestamp)
                for tmp in l_acceleration:
                    l_accx.append(tmp.acc_l_x)
                    l_accy.append(tmp.acc_l_y)
                    l_accz.append(tmp.acc_l_z)
                for tmp in l_gyroscope:
                    l_gyrox.append(tmp.gyro_l_x)
                    l_gyroy.append(tmp.gyro_l_y)
                    l_gyroz.append(tmp.gyro_l_z)
                for tmp in trace:
                    xList.append(tmp.x)
                    yList.append(tmp.y)
                    vList.append(tmp.v)
                track = {
                    "x": xList,
                    "y": yList,
                    "v": vList
                }
                l_pressureList = {
                    "a": l_a,
                    "b": l_b,
                    "c": l_c,
                    "d": l_d
                }
                l_accelerationList = {
                    "x": l_accx,
                    "y": l_accy,
                    "z": l_accz
                }
                l_gyroscopeList = {
                    "x": l_gyrox,
                    "y": l_gyroy,
                    "z": l_gyroz
                }
                r_pressureList = {
                    "a": l_a,
                    "b": l_b,
                    "c": l_c,
                    "d": l_d
                }
                r_accelerationList = {
                    "x": l_accx,
                    "y": l_accy,
                    "z": l_accz
                }
                r_gyroscopeList = {
                    "x": l_gyrox,
                    "y": l_gyroy,
                    "z": l_gyroz
                }

                graph = {
                    "categories": categories,
                    "l_pressure": l_pressureList,
                    "l_acceleration": l_accelerationList,
                    "l_gyroscope": l_gyroscopeList,
                    "r_pressure": r_pressureList,
                    "r_acceleration": r_accelerationList,
                    "r_gyroscope": r_gyroscopeList,
                    "plotLines": plotLines
                }

                result = {
                    "w_summary": w_summary,
                    "track": track,
                    "graph": graph
                }

                return render_to_response('gaitanalysis/detail.html', {'result': simplejson.dumps(result)}, RequestContext(request))

    except Exception as e:
        response = HttpResponse()
        response.write("<script>alert('请先登录'),window.location.href='/homepage/index/'</script>")
        return response


# from pyspark import SQLContext, SparkConf, SparkContext
# def user_info(request):
#     conf = SparkConf().setAppName('ipsapp').setMaster('local')
#     sc = SparkContext(conf=conf)
#     sqlContext = SQLContext(sc)
#     df = sqlContext.load()


def record(request):
    try:
        if request.user.is_authenticated():
            return render_to_response('gaitanalysis/record.html', RequestContext(request))
    except Exception as e:
        response = HttpResponse()
        response.write("<script>alert('请先登录'),window.location.href='/homepage/index/'</script>")
        return response
